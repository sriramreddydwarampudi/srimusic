package com.srimusic.app;

import android.os.Bundle;
import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
import org.kivy.android.PythonActivity;

public class MainActivity extends PythonActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        
        // Initialize Python
        if (!Python.isStarted()) {
            Python.start(new AndroidPlatform(this));
        }
        
        // Run the main.py script
        Python py = Python.getInstance();
        PyObject pyModule = py.getModule("main");
    }
}