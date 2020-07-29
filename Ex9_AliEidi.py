class Time:
    def __init__ (time, Hour = 0, Minute = 0, Second = 0):
        time.Hour = Hour
        time.Minute = Minute
        time.Second = Second
    def show_time (time1):
        return str(time1.Hour)+':'+ str(time1.Minute)+':'+str(time1.Second)
    def __str__ (time1):
        return str(time1.Hour)+':'+ str(time1.Minute)+':'+str(time1.Second)
    def __repr__ (time1):
        return str(time1.Hour)+':'+ str(time1.Minute)+':'+str(time1.Second)
    def __add__ (time1 , time2):
        sumH = time1.Hour + time2.Hour
        sumM = time1.Minute + time2.Minute
        sumS = time1.Second + time2.Second
        if time1.Second > 60:
            sumM += sumS // 60
            sumS = sumS % 60
        if sumM > 60:
            sumH += sumM // 60
            sumM = sumM % 60
        return str(sumH)+':'+ str(sumM)+':'+str(sumS)
    def __sub__ ( time1 , time2):
        if time1.Hour < time2.Hour:
            return 'Error Message'
        if time1.Second < time2.Second:
            timeS = time1.Second +60
            timeS = timeS - time2.Second
            timeM = time1.Minute - 1
        else:
            timeS = time1.Second - time2.Second
            timeM = time1.Minute
        if timeM < time2.Minute:
            timeM += 60
            timeM = timeM - time2.Minute
            timeH = time1.Hour - 1
            timeH = timeH - time2.Hour
        else:
            timeM = time1.Minute - time2.Minute
            timeH = time1.Hour - time2.Hour
        return str(timeH)+':'+ str(timeM)+':'+str(timeS)
    def __eq__ (time1 , time2):
        if time1.Hour == time2.Hour and time1.Minute == time2.Minute and time1.Second == time2.Second:
            return True      
    def __lt__ (time1 , time2):
        if time1.Hour < time2.Hour:
            return   True
        elif time1.Hour > time2.Hour:
            return  False
        else:
            if time1.Minute < time2.Minute:
                return   True
            elif time1.Minute > time2.Minute:
                return  False
            else:
                if time1.Second < time2.Second:
                    return   True
                elif time1.Second > time2.Second:
                    return  False
                else:
                    return False
    def __gt__ (time1 , time2):
        if time1.Hour < time2.Hour:
            return   False
        elif time1.Hour > time2.Hour:
            return  True
        else:
            if time1.Minute < time2.Minute:
                return   False
            elif time1.Minute > time2.Minute:
                return  True
            else:
                if time1.Second < time2.Second:
                    return   False
                elif time1.Second > time2.Second:
                    return  True
                else:
                    return False
    def __le__ (time1 , time2):
        if time1.Hour < time2.Hour:
            return   True
        elif time1.Hour > time2.Hour:
            return  False
        else:
            if time1.Minute < time2.Minute:
                return   True
            elif time1.Minute > time2.Minute:
                return  False
            else:
                if time1.Second < time2.Second:
                    return   True
                elif time1.Second > time2.Second:
                    return  False
                else:
                    return True
    def __ge__ (time1 , time2):
        if time1.Hour < time2.Hour:
            return   False
        elif time1.Hour > time2.Hour:
            return  True
        else:
            if time1.Minute < time2.Minute:
                return   False
            elif time1.Minute > time2.Minute:
                return  True
            else:
                if time1.Second < time2.Second:
                    return   False
                elif time1.Second > time2.Second:
                    return  True
                else:
                    return True   
        
