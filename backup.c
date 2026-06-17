#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string answer = get_string("What's yor name? ");
    printf("Hello, %s\n", answer);
}
