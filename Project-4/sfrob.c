#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdlib.h>

void CheckMemorySpace (int *buffer_iterator, int *memory_size, char** word_buffer);
int prep_frobcmp(const void* a, const void* b);

int my_compare(char *const *l, char *const *r) {
    return strcmp(*l, *r);
}

int frobcmp (char const* a, char const* b)
{
    int i = 0;
    char end1 = ' ';
    char end2 = ' ';
    int flag_words = 1;
    int a_len = strlen(a);
    int b_len = strlen(b);
    
    //printf("a: %s, b: %s, a_len: %d, b_len: %d", a, b, a_len, b_len);
    while (i < a_len && i < b_len) {
        char char1 = a[i]^42;
        char char2 = b[i]^42;
        
        if (char1 > char2)
        {
            //printf("exiting");
            return 1;
        }
        else if (char1 < char2)
        {
            //printf ("exiting negative");
            return -1;
        }
        i++;
    }
    
    //printf("out of while loop");
    
    if (a_len > b_len)
    {
        return 1;
    }
    else if (a_len < b_len)
    {
        return -1;
    }
    else
    {
        return 0;
    }
    
//    while (a[i] != ' ' && b[i] != ' ' && a[i] != 0 && b[i] != 0)
//    {
//        char char1 = a[i]^42;
//        char char2 = a[i]^42;
//
//        
//    }
//    {
//        char char1 = a[i]^42;
//        char char2 = a[i]^42;
//        
//        if (strcmp(a, b) != 0)
//        {
//            flag_words = 0;
//            
//            if (a[i] != ' ' && b[i] != ' ')
//            {
//                if (char1 < char2)
//                {
//                    return -1;
//                }
//                else if (char1 > char2)
//                {
//                    return 1;
//                }
//            }
//        }
//        i++;
//        end1 = a[i];
//        end2 = b[i];
//    }
//    if (flag_words == 1 && end1 != ' ' && end2 == ' ')
//    {
//        return 1;
//    }
//    else if (flag_words == 1 && end1 == ' ' && end2 != ' ')
//    {
//        return -1;
//    }
//    else
//    {
//        return 0;
//    }
//}
}

int main(void)
{
    // counter of words
    int counter = 0;
    // declare memory size
    int memory_size = 100;
    // create the buffer based on memory_size
    char* word_buffer = (char*)malloc( (sizeof(char))*(memory_size) );
    // grab the first character
    char current_charater = getchar();
    int buffer_iterator = 0;
    char end_of_word = ' ';
    // current word is a list with the current word
    //char curr_word = "";
    // will iterate through curr_word
    //int curr_word_counter = 0;
    // initialize actual_words
    //char** actual_words = (char**)malloc(sizeof(char*)*counter);
    // iterate through actual_words
    //int actual_words_counter = 0;
    
    while (current_charater != EOF)
    {
    CheckMemorySpace (&buffer_iterator, &memory_size, &word_buffer);
        if (current_charater == end_of_word)
            {
                //set actual_words equal to the characters in curr_word
                //actual_words[actual_words_counter] = curr_word;
                //iterate to the next one in actual_words
                //actual_words_counter++;
                // add the current character to the buffer
                word_buffer[buffer_iterator] = current_charater;
                // you move to the next empty space in the buffer
                buffer_iterator = buffer_iterator + 1;
                // add 1 to counter because you're at the end of a word
                counter = counter + 1;

                //delete everything in curr_word
                //curr_word = "";
                //curr_word_counter = 0;
            }
        
        else
            {
                // add the current character to the buffer
                word_buffer[buffer_iterator] = current_charater;
                //curr_word = curr_word + current_charater;
                //curr_word_counter ++;
                // you move to the next empty space in the buffer
                buffer_iterator = buffer_iterator + 1;
            }
        // grab the next character
        current_charater = getchar();
    }
    

    CheckMemorySpace (&buffer_iterator, &memory_size, &word_buffer);
    
    // insert space at the end of the buffer
    if (word_buffer[buffer_iterator-1] != ' ')
    {
        word_buffer[buffer_iterator] = '\0';
        counter++;
    }
    
    //printf("word_buffer: %s\n", word_buffer);
    
    if (ferror(stdin))
    {
        fprintf(stderr, "couldn't read in all the words");
        exit(1);
    }
    
    char** actual_words = (char**)malloc(sizeof(char*)*counter);
    
    if (actual_words == NULL)
	{
fprintf(stderr, "error allocating memory");
        exit(1);
	} 


    for (int i = 0;i<counter;i++) {
        actual_words[i] = (char*)malloc(memory_size * sizeof(char*));
          if (actual_words[i] == NULL)
        {
	fprintf(stderr, "error allocating memory");
        exit(1);
        }

	//memset(actual_words[i], 0, memory_size);
    }


    int i = 0;
    char *s;
    int s_count;
    while (i < counter)
    {
        //printf("in word separator loop");
        s = actual_words[i];
        s_count = 0;
        while (*word_buffer != ' ' && *word_buffer != 0)
        {
            s[s_count] = *word_buffer;
            s_count++;
            word_buffer++;
        }
        s[s_count] = 0;
        if (*word_buffer == ' ')
        {
            word_buffer++;
        }
        i++;
    }
//    int iterator2 = 0;
//    int buffer_counter2;
//    // do this for the number of words there are
//    while (iterator2 < counter)
//    {
//        // add the words from buffer
//        buffer_counter2 = 0;
//        //actual_words[iterator2] = word_buffer;
//        // check if it's the end of a word, which is denotated by a ' '
//        while ( *word_buffer != ' ')
//        {
//            // make sure that this isn't the last word
////            if (iterator2 + 1 != counter)
////            {
////                printf("counter: %d", counter);
////                // increase the word buffer by 1
////                actual_words[iterator2][buffer_counter2] = *word_buffer;
////                buffer_counter2++;
////                word_buffer++;
////            }
////            else
////            {
////                break;
////            }
//            printf("counter: %d, word_buffer: %c", counter, *word_buffer );
//            // increase the word buffer by 1
//            actual_words[iterator2][buffer_counter2] = *word_buffer;
//            buffer_counter2++;
//            word_buffer++;
//        }
//        // go to the next word
//        iterator2 = iterator2 + 1;
//        word_buffer++;
//        //while( *word_buffer == ' ' && *word_buffer != 0) word_buffer++;
//    }
    
//    printf("\ndebug\n");
//    for (int i = 0;i<counter;i++) {
//        printf("word %d: %s", i, actual_words[i]);
//    }
//    printf("\nend debug\n");
    
        char* to_print;
    
    //printf("about to qsort");
    
    qsort(actual_words, counter, sizeof(char*), prep_frobcmp);
    
    //printf("after qsort");
//    printf("\ndebug\n");
//    for (int i = 0;i<counter;i++) {
//        printf("word %d: %s", i, actual_words[i]);
//    }
//    printf("\nend debug\n");
    
    for (int final = 0; final < counter; final ++)
    {
        to_print = actual_words[final];
        //putchar(*to_print);
        
        while (*to_print != ' ' && *to_print != '\0' && to_print != NULL)
        {
	    putchar (*to_print); 
            to_print = to_print + 1;
            //putchar(*to_print);
        }
        putchar(' ');
    }
    
    	
    if (ferror(stdout))
    {
        fprintf(stderr, "error printing characters");
        exit(1);
    }

     for (int i = 0;i<counter;i++) {
        //actual_words[i] = (char*)malloc(memory_size * sizeof(char*));
        free (actual_words[i]); 
	//memset(actual_words[i], 0, memory_size);
    }
     free (actual_words); 
    
    return 0;
}


void CheckMemorySpace (int *buffer_iterator, int *memory_size, char** word_buffer)
{
    if (*buffer_iterator == *memory_size)
    {
        *memory_size = *memory_size * 2;
        *word_buffer = (char*)realloc(*word_buffer, *memory_size);
    }
}

int prep_frobcmp(const void* a, const void* b)
{
    return frobcmp( *((char**)a), *((char**)b) );
}
