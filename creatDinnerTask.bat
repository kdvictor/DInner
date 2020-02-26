SCHTASKS /Delete /TN dinner /F
SCHTASKS /Create /SC WEEKLY /D "TUE FRI THU SAT MON WED " /ST 11:00 /TN dinner /TR E:\DInner\runDinner.exe