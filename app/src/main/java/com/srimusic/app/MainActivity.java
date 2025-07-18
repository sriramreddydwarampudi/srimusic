package com.srimusic.app;

import android.os.Bundle;
import androidx.appcompat.app.AppCompatActivity;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Initialize Python
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        
        // Run the main.py script
        Python py = Python.getInstance();
        PyObject mainModule = py.getModule("main");
        PyObject mainActivity = mainModule.callAttr("SriMusicApp");
        mainActivity.callAttr("run");
    }
}