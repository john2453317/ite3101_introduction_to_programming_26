def shut_down(shut_down:'s')"Shutting down"
    return shut_down
    
    if yes():
        speak("Shutting down") 
    elif "no"():
        speak("Shutdown aborted") 
    else:
        speak ("Sorry")