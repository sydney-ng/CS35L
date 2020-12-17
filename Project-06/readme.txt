1. Issues I ran into: 
   - For the laboratory, the hardest part was trying
     to get --parallel to work. It kept telling me that 
     sort: unrecognized option '--parallel=1'
     Try `sort --help' for more information.
     This is because I was not running it on lnxsrv09. 
     Once I logged onto this server, it worked perfectly. 
   - For the homework, the hardest part was understanding
     the code that already exists. I wasn't too familiar with
     C and I had trouble understanding what each of the functions 
     with commands like mul and accessing pointers with -> etc. I 
     looked up the commands, which then made it easier to understand.
   - Also, I had a hard time trying to decide how to structure 
     the code. At first I had tried to create a struct and then pass
     all the variables (ex. scene, thread IDs etc.) using the struct.
     However, this got too complicated. I made variables global and 
     only needed to give the pthread function the current thread to 
     be processed. 
2. Conclusions about SRT improving performance: 
    - Using SRT will improve how fast your program runs by dividing 
      the workload among threads.
    - Example: With one thread, you get: 
      real	0m27.068s
      user	0m27.021s
      sys	0m0.033s
    - Example: With 8 threads, you get: 
      real	0m5.856s
      user	0m44.671s
      sys	0m0.034s
    - As you can see, 8 threads is significantly faster than 1 thread. 
