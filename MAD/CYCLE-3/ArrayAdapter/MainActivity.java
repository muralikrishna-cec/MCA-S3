package com.example.newarrayadapter;

import static com.example.newarrayadapter.R.id.listView;

import androidx.appcompat.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.ArrayAdapter;
import android.widget.ListView;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        
        ListView listView=findViewById(R.id.listView);

        String [] fruits={"Apple","Banana","Cherry","Dates","Grape","Kiwi","Lemon","Mnago","Orange","Peach"};

        ArrayAdapter<String>adapter=new ArrayAdapter<>(this
                ,android.R.layout.simple_list_item_1,fruits);
                
        listView.setAdapter(adapter);
    }
}