# PoyntOS Emulator
## Description
To help streamline your Poynt app development, we have provided the PoyntOS Emulator. The emulator
can be installed on virtual devices (i.e. Android Studio's AVD, Genymotion, etc.) or on any 7"
Android tablet.

---

## Using AVD in Android Studio?
If you're using AVD (Android Virtual Device Manager in Android Studio), we have packaged a
pre-configured device image of the PoyntOS Emulator. AVD provides many knobs and levers and
using this package should guarantee a smooth running PoyntOS emulator with minimal effort. 
Navigate to the [`_INSTALL_ANDROID_STUDIO_AVD`](/_INSTALL_ANDROID_STUDIO_AVD) folder in this package
and review the instructions in README.

---

## Using a different emulator or a physical tablet?
If you're using an emulator other than AVD (like Genymotion) _or_ you want to install the PoyntOS
emulator on a physical device, we have provided a script that installs PoyntOS to your device using
the `adb` command line tool. 
Navigate to the [`_INSTALL_WITH_ADB`](/_INSTALL_WITH_ADB) folder in this package and review the instructions in 
README.

---

## Want your own developer-edition Poynt Smart Terminal device?
Alternatively, if you would like to order a Poynt Dev Kit, which includes an actual Poynt Smart Payment Terminal,
you can order one from the [PoyntHQ Developer Portal](https://poynt.net/devkits/order). It is a fully functional
terminal allowing you to side-load, test and debug your apps and perform card-based test transactions.
