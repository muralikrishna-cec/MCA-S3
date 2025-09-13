package com.example.login_form;

import static com.example.login_form.R.id.pwd;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    protected static final String VALID_USR="user";
    protected static final String VALID_pass="pass";
    private EditText username;
    private EditText password;
    private Button login;


    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        username=findViewById(R.id.uname);
        password=findViewById(R.id.pwd);
        login=findViewById(R.id.lgn);

        login.setOnClickListener(view ->{
            
            String enteredUname=username.getText().toString().trim();
            String enteredPass=password.getText().toString().trim();

            if(enteredUname.isEmpty() || enteredPass.isEmpty()){
                showToast("Please enter both details..");
            } else if(isValid(enteredUname,enteredPass)){
                showToast("Login Success...");
            } else {
                showToast("Invalid Credentials...");
            }
        });
    }

    private boolean isValid(String euname, String epass) {
        return VALID_USR.equals(euname) && VALID_pass.equals(epass);
    }

    private void showToast(String msg) {
        Toast.makeText(this,msg,Toast.LENGTH_LONG).show();
    }
}