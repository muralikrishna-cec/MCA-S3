
import androidx.appcompat.app.AlertDialog;
import androidx.appcompat.app.AppCompatActivity;

import android.database.Cursor;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

public class MainActivity extends AppCompatActivity {

    DatabaseHelper myDb;
    EditText editTextId, editTextName, editTextEmail;
    Button btnAdd, btnView, btnUpdate, btnDelete;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

// Create an instance of the DatabaseHelper
        myDb = new DatabaseHelper(this);

// Initialize UI components
        editTextId = findViewById(R.id.editTextId);
        editTextName = findViewById(R.id.editTextName);
        editTextEmail = findViewById(R.id.editTextEmail);
        btnAdd = findViewById(R.id.btnAdd);
        btnView = findViewById(R.id.btnView);
        btnUpdate = findViewById(R.id.btnUpdate);
        btnDelete = findViewById(R.id.btnDelete);

// Set up button listeners
        addData();
        viewAll();
        updateData();
        deleteData();
    }
// Method to handle the "ADD" button click

    public void addData() {
        btnAdd.setOnClickListener(
                new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isInserted = myDb.insertData(
                        editTextName.getText().toString(),
                        editTextEmail.getText().toString()
                );
                if (isInserted) {
                    Toast.makeText(MainActivity.this, "Data Inserted Successfully!",
                            Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Data Insertion Failed",
                            Toast.LENGTH_SHORT).show();
                }
            }
        }
        );
    }

// Method to handle the "VIEW ALL" button click
    public void viewAll() {
        btnView.setOnClickListener(
                new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Cursor res = myDb.getAllData();
                if (res.getCount() == 0) {
// Show message if no data is found
                    showMessage("Error", "Nothing found");

                    return;
                }

                StringBuffer buffer = new StringBuffer();
                while (res.moveToNext()) {
                    buffer.append("ID: " + res.getString(0) + "\n");
                    buffer.append("Name: " + res.getString(1) + "\n");
                    buffer.append("Email: " + res.getString(2) + "\n\n");
                }
// Show all data in a dialog
                showMessage("Data", buffer.toString());
            }
        }
        );
    }

// Method to handle the "UPDATE" button click
    public void updateData() {
        btnUpdate.setOnClickListener(
                new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                boolean isUpdated = myDb.updateData(
                        editTextId.getText().toString(),
                        editTextName.getText().toString(),
                        editTextEmail.getText().toString()
                );
                if (isUpdated) {
                    Toast.makeText(MainActivity.this, "Data Updated Successfully!",
                            Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Data Update Failed",
                            Toast.LENGTH_SHORT).show();
                }
            }
        }
        );
    }

// Method to handle the "DELETE" button click
    public void deleteData() {
        btnDelete.setOnClickListener(
                new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Integer deletedRows = myDb.deleteData(editTextId.getText().toString());
                if (deletedRows > 0) {
                    Toast.makeText(MainActivity.this, "Data Deleted Successfully!",
                            Toast.LENGTH_SHORT).show();
                } else {
                    Toast.makeText(MainActivity.this, "Data Deletion Failed",
                            Toast.LENGTH_SHORT).show();
                }
            }
        }
        );
    }

// Generic method to show a message dialog
    public void showMessage(String title, String message) {
        AlertDialog.Builder builder = new AlertDialog.Builder(this);
        builder.setCancelable(true);
        builder.setTitle(title);
        builder.setMessage(message);
        builder.show();
    }
}
