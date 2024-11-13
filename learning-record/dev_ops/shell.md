### print
`echo "Hello, Shell" `
`printf "Hello, Shell" `

### To replace an entire line in a file containing specific keywords using sed
`sed -i '/keyword/s/.*/replacement_text/' filename`

### loop 
`for i in {1..10}`

### sleep
`sleep .5` # Waits 0.5 second.
`sleep 5`  # Waits 5 seconds.
`sleep 5s` # Waits 5 seconds.

### $? details
In a Unix or Linux shell, $? is a special variable that holds the exit status of the last command executed. The exit status is a number that indicates whether the command completed successfully:
`0` usually means the command was successful.
`Any other number (typically 1-255)` means the command encountered an error or failed for some reason.

### Shell Basic Operators`
`-eq`  Checks if the value of two operands are equal or not; if yes, then the condition becomes true.	
`-ne`  Checks if the value of two operands are equal or not; if values are not equal, then the condition becomes true.