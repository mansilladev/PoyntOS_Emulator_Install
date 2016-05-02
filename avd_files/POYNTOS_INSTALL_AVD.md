# PoyntOS Emulator for Android Virtual Device (AVD)
## Description
This is a packged version of the Poynt Emulator built using Android Studio 2.0 AVD. The emulator image 
is based on Android API 19 / KitKat 4.4.4. The PoyntOS emulator has been pre-installed and is ready to be 
activated on your Poynt developer account.

## Using a different virtual device emulator like Genymotion?
If you're using a different emulator (not Android Studio's AVD), do not follow the instructions below.
Instead, read the `POYNTOS_INSTALL_ADB.md` instructions in the `adb_files` folder.

---

## Pre-requisites for the Poynt Emulator for AVD
 * Install the Android 4.4 (KitKat) SDK. In Android Studio by navigating to `Tools` > `Android` > `SDK Manager`.
 * Locate Android Studio's `avd` folder. More instructions for locating this folder are below.
 * Python (if you're using the installtion script)
 
## Installation Instructions for AVD
There are two ways to install the AVD emulator.
 * Setup script
  1. Run the `setup_poyntos_avd.py` Python script.
  2. Type in the path to your Android Studio's `avd` folder.
  3. In Android Studio, navigate to `Tools` > `Android` > `AVD Manager`. If you don't see `Poynt Emulator 1.2.11` in the list of devices, click the refresh button at the bottom of the window. If you still do not see it, then you did not provide the correct path to your Android Studio's `avd` folder.
  
 * Manual installation
  1. Copy the contents of this package's `avd_files` folder into your Android Studio's `avd` folder. Instructions for locating your `avd` folder are below.
  2. Edit each of the `.ini` files with the correct path to your Android Studio's `avd` folder. Replace `%%AVD_

## Ready to Go!
Now that PoyntOS is installed, the first thing you'll need to do is activate the terminal. Run `SetupWizard` to start the Activation flow. 
At this point, you'll need to have set up a test merchant and added a test terminal from the PoyntHQ Developer Portal. For more information 
about setting up a test merchant, please read the [tutorial on setting up PoyntOS](https://poynt.github.io/developer/tut/setup-poyntos.html).

---

## Where is my *avd* folder in Android Studio?
The folder location will vary depending on your operating system, as well as _how_ you installed the Android Studio. You can easily find the location by launching the Android Virtual Device Manager, and from an exisiting image, select `Show on Disk` from `Actions`.

#### Mac OS X
On most Mac installations, the `avd` folder is located here: `/Users/{username}/.android/avd`

#### Windows
On most Windows installations, the `avd` folder is located here: `/Documents and Settings/{username}/.android/avd`

---

## Caveats
 * You can only run a single instance of the Poynt emulator at a time. If you try to run simultaneous instances, those instances will likely run stock blank images.
 * Editing the configuration in AVD may cause problems, such as a resized `userdata.img` (down to 200MB from 1GB). There is a known bug in AVD where that image file keeps being reset to 200MB despite the configuration being set to 1GB. If this occurs, you can ignore, just as long as your `userdata-qemu.img` file remains 1GB (this is the actual image used by AVD).
   
---

## Support
Having problems getting the Poynt emulator installed or running properly? Head over to the [Poynt Developer Forums](https://discuss.poynt.net/c/developers) and our team can help you out.