# PoyntOS Emulator Installation via ADB
## Description
If you're using alternative emulator to Android Studio's AVD, such as Genymotion, or you have a 
physical Android tablet you'd like to use as a testing device, follow the instructions below.

Alternatively, if you would like to order a Poynt Dev Kit, which includes an actual Poynt Smart Payment Terminal,
you can order one from the [PoyntHQ Developer Portal](https://poynt.net/devkits/order). It is a fully functional
terminal allowing you to sideload your apps and perform card-based test transactions.

## Pre-requisites for the PoyntOS Emulator
 * For virtual emulators, create a new virtual device built on Android API 19 (KitKat/4.4.4), tablet form-factor, 800x1200 resolution
 * For a physical tablet, use a 7" Android tablet
 * ADB (Android Debug Bridge) command line tool - see http://developer.android.com/tools/help/adb.html
 * Python (to run the installation script)

## Installation Instructions
 1. Verify that all virtual devices are disconnected using `adb devices`. If you have devices connected, disconnect them. If devices are still being shown, reset adb with `adb kill-server`.
 2. Launch the new virtual device
 3. Verify that the new virtual device is the _only_ visible device in `adb devices`
 4. Run the `setup_poyntos_adb.py` Python script (ex: `python setup_poyntos_adb.py`)

You may see warnings or failure messages, as the script will try to uninstall any previously installed PoyntOS packages. You can ignore these messages.

## Ready to Go!
Now that PoyntOS is installed, the first thing you'll need to do is activate the terminal. Run `SetupWizard` to start the Activation flow. 
At this point, you'll need to have set up a virtual store and virtual terminal in the PoyntHQ Developer Portal. For more information, please
read the [tutorial on setting up PoyntOS](https://poynt.github.io/developer/tut/setup-poyntos.html).

---
## Support
Having problems getting the PoyntOS emulator installed or running properly? Head over to the [Poynt Developer Forums](https://discuss.poynt.net/c/developers) and our team can help you out.
