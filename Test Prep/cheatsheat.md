## What data structure to use

### Queue (FIFO)

**Best option:** `collections.deque` (fast at the front)

* **Enqueue (add to back):** `q.append(x)`
* **Dequeue (remove from front):** `q.popleft()`
* **Add to front (priority / undo):** `q.appendleft(x)`
* **Empty check:** `if not q:`

> Using a normal list queue with `pop(0)` works, but it’s slower (shifts everything). Deque is the “correct” tool.

### Stack (LIFO)

Use a normal list:

* **Push (add to top):** `stack.append(x)`
* **Pop (remove most recent):** `stack.pop()`
* **Peek top (look only):** `stack[-1]` (only if not empty)
* **Empty check:** `if not stack:`

## 2) Required behaviors (translate to operations)

### A. `place_order(order_id)`

* Queue: add to end
  ✅ `dispatch.append(order_id)`

### B. `ship_next()`

* If queue empty → message
* Else: remove from **front of queue**, push onto **top of stack**
  ✅ `order = dispatch.popleft()` then `shipped.append(order)`

### C. `cancel_last_shipment()` (Undo)

* If stack empty → message
* Else: pop from stack, insert to **front of queue**
  ✅ `order = shipped.pop()` then `dispatch.appendleft(order)`

### D. `view_manifest()`

* Print queue and stack state (loop-based display is often required)

## 3) Common exam pitfalls (quick checklist)

* FIFO = **remove oldest** → front of queue (`popleft()` or `pop(0)`)
* LIFO = **remove newest** → end of list (`pop()`)
* Always handle empty structures before removing
* “Undo last shipment” usually means **stack pop → queue front**
* If asked to “use a loop”, actually loop through the items when printing


```python
from collections import deque

# Queue: first in, first out
dispatch_queue = deque()

# Stack: last in, first out
shipped_stack = []


def place_order(order_id: str) -> None:
    dispatch_queue.append(order_id)
    print(f"Order received: {order_id} added to queue.")


def ship_next() -> None:
    if not dispatch_queue:
        print("No pending orders to ship.")
        return

    order = dispatch_queue.popleft()     # FIFO
    shipped_stack.append(order)          # push to stack (LIFO)
    print(f"Shipped: {order} loaded onto truck.")


def cancel_last_shipment() -> None:
    if not shipped_stack:
        print("No shipped orders to cancel.")
        return

    order = shipped_stack.pop()          # pop most recent shipment
    dispatch_queue.appendleft(order)     # goes to FRONT of line
    print(f"Shipping Cancelled: {order} returned to front of line.")


def view_manifest() -> None:
    print("\n=== MANIFEST ===")

    print("To Be Shipped (Queue - front to back):")
    if not dispatch_queue:
        print("  (empty)")
    else:
        i = 1
        for item in dispatch_queue:      # loop to display
            print(f"  {i}. {item}")
            i += 1

    print("On The Truck (Stack - bottom to top):")
    if not shipped_stack:
        print("  (empty)")
    else:
        i = 1
        for item in shipped_stack:       # loop to display
            print(f"  {i}. {item}")
            i += 1

    print("==============\n")


def main() -> None:
    while True:
        print("1. Place New Order")
        print("2. Ship Next Order")
        print("3. Cancel Last Shipment (Undo)")
        print("4. View Manifest")
        print("5. Exit System")
        choice = input("Select Option: ").strip()

        if choice == "1":
            order = input("Enter Order ID/Details: ").strip()
            if order == "":
                print("Order cannot be blank.")
            else:
                place_order(order)

        elif choice == "2":
            ship_next()

        elif choice == "3":
            cancel_last_shipment()

        elif choice == "4":
            view_manifest()

        elif choice == "5":
            print("System shutting down...")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
```

## 5) Ultra-short “operations map” (memorize this)

* **Queue enqueue:** `append(x)`
* **Queue dequeue:** `popleft()`
* **Queue add-front:** `appendleft(x)`
* **Stack push:** `append(x)`
* **Stack pop:** `pop()`

```py
# Queue (FIFO) using a list
dispatch_queue = []

# Stack (LIFO) using a list
shipped_stack = []


def place_order(order_id: str) -> None:
    dispatch_queue.append(order_id)  # enqueue (back)
    print(f"Order received: {order_id} added to queue.")


def ship_next() -> None:
    if len(dispatch_queue) == 0:
        print("No pending orders to ship.")
        return

    order = dispatch_queue.pop(0)     # dequeue (front)
    shipped_stack.append(order)       # push to stack
    print(f"Shipped: {order} loaded onto truck.")


def cancel_last_shipment() -> None:
    if len(shipped_stack) == 0:
        print("No shipped orders to cancel.")
        return

    order = shipped_stack.pop()       # pop most recent
    dispatch_queue.insert(0, order)   # return to FRONT of queue
    print(f"Shipping Cancelled: {order} returned to front of line.")


def view_manifest() -> None:
    print("\n=== MANIFEST ===")

    print("To Be Shipped (Queue - front to back):")
    if len(dispatch_queue) == 0:
        print("  (empty)")
    else:
        for i in range(len(dispatch_queue)):
            print(f"  {i+1}. {dispatch_queue[i]}")

    print("On The Truck (Stack - bottom to top):")
    if len(shipped_stack) == 0:
        print("  (empty)")
    else:
        for i in range(len(shipped_stack)):
            print(f"  {i+1}. {shipped_stack[i]}")

    print("==============\n")


def main() -> None:
    while True:
        print("1. Place New Order")
        print("2. Ship Next Order")
        print("3. Cancel Last Shipment (Undo)")
        print("4. View Manifest")
        print("5. Exit System")
        choice = input("Select Option: ").strip()

        if choice == "1":
            order = input("Enter Order ID/Details: ").strip()
            if order == "":
                print("Order cannot be blank.")
            else:
                place_order(order)

        elif choice == "2":
            ship_next()

        elif choice == "3":
            cancel_last_shipment()

        elif choice == "4":
            view_manifest()

        elif choice == "5":
            print("System shutting down...")
            break

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
```
