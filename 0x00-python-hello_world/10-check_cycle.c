#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - checks if a singly linked list has a cycle in it
* @list: pointer to the head of the linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
*/
int check_cycle(listint_t *list)
{
listint_t *tortoise = list;
listint_t *hare = list;

while (hare && hare->next)
{
tortoise = tortoise->next;
hare = hare->next->next;
if (tortoise == hare)
return (1);
}

return (0);
}
