import time
import psutil
import pygetwindow as gw



def switch_focus_to_app():
    global jiggles, skips, notfound
    try:
        for process in psutil.process_iter(attrs=['pid', 'name']):
            if process.name().lower() == 'teams.exe' or process.name().lower() == 'ms-teams.exe':
                tw = ""
                for _, title in get_teams_windows():
                    tw = title
                    break
                app_window = gw.getWindowsWithTitle(tw)
                if app_window:
                    #Jiggle only if window is not already active and maximized (most likely already in focus)
                    if app_window[0].isActive and app_window[0].isMaximized:
                        skips = skips + 1
                        print(f"Jiggle skipped {skips} times")
                    else:
                        #If it's minimized - restore, which will take focus
                        if app_window[0].isMinimized:
                            app_window[0].restore()
                        else:
                            #If not minimized - activate
                            app_window[0].activate()
                        time.sleep(2)
                        app_window[0].minimize()
                        jiggles = jiggles + 1
                        print(f"Jiggled Teams {jiggles} times")
                    return True
        notfound = notfound + 1
        print(f"Teams was not found {notfound} times")
    except Exception as e:
        print("There was some error but we up: ", e)
    return False


def get_teams_windows():
    windows = gw.getAllWindows()
    teams_windows = []
    for win in windows:
        hwnd = win._hWnd
        window_title = win.title
        if "Microsoft Teams" in window_title:
            teams_windows.append((hwnd, window_title))
    return teams_windows



def main():
    global jiggles, skips, notfound
    jiggles = 0
    skips = 0
    notfound = 0
    waitfor = 2 * 60
    waitforOrig = waitfor
    print(f"Teams Jiggler initiated")
    while True:
        time.sleep(waitfor)

        if switch_focus_to_app():
            waitfor = waitforOrig
        else:
            waitfor = 30


if __name__ == "__main__":
    main()
