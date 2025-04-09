/**
 * You are given the heads of two sorted linked lists list1 and list2.

 Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

 Return the head of the merged linked list.

 */
function mergeTwoLists(list1, list2) {
    let i = 0, j = 0, mergedList = [];
    while (i < list1.length && j < list2.length) {
        if (list1[i] <= list2[j]) {
            mergedList.push(list1[i])
            i++;
        } else {
            mergedList.push(list2[j])
            j++;
        }
    }
    while (i < list1.length) {
        mergedList.push(list1[i])
        i++;
    }
    while (j < list2.length) {
        mergedList.push(list2[j])
        j++;
    }
    return mergedList;
}

// Example usage:
const list1 = [1, 2, 3, 6, 8, 9]
const list2 = [4, 5, 7, 10];

const mergedList = mergeTwoLists(list1, list2);
console.log(mergedList); // The head of the merged linked list
