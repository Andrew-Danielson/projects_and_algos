class SLLNode {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class SLL {
    constructor() {
        this.head = null;
    }
    addFront(value) {
        let addNode = new SLLNode(value);
        addNode.next = this.head;
        this.head = addNode;
        return this.head
    }
    removeFront() {
        if (this.head == null) {
            return this.head;
        }
        let removeNode = this.head;
        this.head = removeNode.next;
        removeNode.next = null;
        return this.head;
    }
    front() {
        if (this.head == null) {
            return null;
        }
        else {
            return this.head.value;
        }
        // return this.head == null ? null : this.head.value;
    }
    display() {
        let str = "";
        if (this.head == null) {
            return "null";
        }
        str += this.head.value;
        let runner = this.head.next;
        while (runner != null) {
            str + ", " + runner.value;
            runner = runner.next;
        }
        return str;
    }
}

let newSLL = new SLL();
newSLL.addFront(10);
// newSLL.removeFront();
newSLL.addFront(55);
newSLL.addFront(35);
// console.log(newSLL.display());
console.log(newSLL);
console.log(newSLL.front());
