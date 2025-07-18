# Add project specific ProGuard rules here.
# You can control the set of applied configuration files using the
# proguardFiles setting in build.gradle.
#
# For more details, see
#   http://developer.android.com/guide/developing/tools/proguard.html

# Keep Python classes
-keep class org.python.** { *; }
-keep class com.chaquo.python.** { *; }

# Keep Kivy classes
-keep class org.kivy.** { *; }

# Keep app classes
-keep class com.srimusic.app.** { *; }