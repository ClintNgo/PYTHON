class ListNode {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

var x = new ListNode("DisneyLand");
console.log(x)

var y = new ListNode("Las Vegas");
x.next = y;
console.log

var z = new ListNode("Yellowstone");
y.next = z;
console.log

class SinglyLinkedList {
    constructor(){
        this.head = null;
        this.tail = null;
    }
}

addToFront(value){

}

addToBack(value){

}

contains(value){

}

display(){
    if (this.head == null){
        return null;
    }
}

    var values = this.head.value;
    var runner = this.head.next;

    while (runner != null){
        values += "-" + runner.value;
        runner = runner.next;
    }

    return values;