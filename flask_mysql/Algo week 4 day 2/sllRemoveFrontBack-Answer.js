// Today we will be removing from the front and back of the SLL using the functions found at the bottom
// 


class ListNode {
    constructor(value) {
      this.value = value;
      this.next = null;
    }
}

class SinglyLinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
    }

    addToFront(value) {
        var new_node = new ListNode(value);

        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            new_node.next = this.head;
            this.head = new_node;
        }
    }

    addToBack(value) {
        var new_node = new ListNode(value);

        if (this.head == null) {
            this.head = new_node;
            this.tail = new_node;
        }

        else {
            this.tail.next = new_node;
            this.tail = new_node;
        }
    }

    contains(target) {
        var runner = this.head;

        while (runner != null) {
            if (runner.value == target) {
                return true;
            }
            runner = runner.next;
        }
        return false;
    }
    
    display() {
        if (this.head == null) {
            return null;
        }
        var values = this.head.value;
        var runner = this.head.next;

        while (runner != null) {
            values += " - " + runner.value;
            runner = runner.next;
        }
        return values;
    }

    // Use removeFront() to remove the head of the linked list and return its value
    // HINTS: 
    // this needs to be in a certain order, what would happen if you set this.head's value to null first?
    // or what would happen if you only set the new head and that's it?  
    // this.head's value needs to change
    // The connection between the old head and new head needs to be severed
    // If you get done early try and handle the edge cases if the linked list only has one or zero nodes

    removeFront() {
        if (this.head == null) { //if list is empty
            return null;
        }
        else if (this.head == this.tail) { //if there's one item in the list
            var temp = this.head; //saves the single item into temp
            this.head = null; //sets the head to null which empties list
            this.tail = null; //sets tail to null which empties list
            return temp.value; //returns the value we stored at the beginning
        }

        var temp = this.head //stores current head into temp
        this.head = this.head.next //sets head to the 2nd node in list
        temp.next = null //sets the next property of the old head to null cutting the connection from the list

        return temp.value
    }

    // Use removeBack() to remove the tail of the linked list and return its value
    // HINTS: 
    // Think about how can we get to the end of the list and how can we tell which one is the 2nd to last?
    // This needs to be in a certain order as well
    // Save the value of the old tail so you can return it  
    // A new tail should be marked
    // The connection between the old tail and new tail needs to be severed
    // If you get done early try and handle the edge cases if the linked list only has one or zero nodes

    removeBack() {
        if (this.head == null) {
            return null;
        }

        else if (this.head == this.tail) {
            var temp = this.head;
            this.head = null;
            this.tail = null;
            return temp.value;
        }

        let runner = this.head; //starts the runner at the beginning
        while (runner != this.tail) { //as long as runner is not equal to the tail keep going
            if (runner.next == this.tail) { //if the next node is the tail (end). This finds the 2nd to last node
                let getEnd = this.tail; // store the last node in getEnd
                this.tail = runner; // set tail to what runner is (the 2nd to last node)
                runner.next = null; // cut the connection of the 2nd to last node and the last node
                return getEnd.value; // return the value of the node removed from the list
            }
            runner = runner.next;  // runner goes to the next node letting the loop progress through the list
        }
    }
}

var new_sll = new SinglyLinkedList();
new_sll.addToBack("Disneyland");
new_sll.addToBack("Las Vegas");
new_sll.addToBack("Mount Rushmore");
new_sll.addToBack("Times Square");
console.log(new_sll.display());

console.log(new_sll.removeFront())
console.log(new_sll.display());

console.log(new_sll.removeBack())
console.log(new_sll.display());
