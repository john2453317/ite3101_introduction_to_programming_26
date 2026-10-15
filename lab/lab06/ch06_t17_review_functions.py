def shut_down(shut_down:'s')
    return shut_down
    
    if yes():
        return "Shutting down"
    elif "no"():
        speak() "Shutdown aborted"
    else:
        speak "Sorry"