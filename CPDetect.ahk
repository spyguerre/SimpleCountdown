Loop {
    Loop, 8 {
        ImageSearch, _, _, 0, 0, A_ScreenWidth, A_ScreenHeight, *42 CPpng/CP%A_Index%.png
        if (ErrorLevel = 0) {
            ImageSearch, _, _, 0, 0, A_ScreenWidth, A_ScreenHeight, *50 CPpng/ValidateCP%A_Index%.png
            if (ErrorLevel = 0) {
                FileRead, WhichCPContent, WhichCP.txt
                if ((A_Index != 1) && (WhichCPContent != A_Index)) {
                    SoundPlay, SFX/check.wav
                }
                if ((A_Index == 1) && (WhichCPContent != A_Index)) {
                    SoundPlay, SFX/fail.wav
                }
                FileDelete, WhichCP.txt
                FileAppend, %A_Index%, WhichCP.txt
            }
        }
    }

    Sleep 150
}
