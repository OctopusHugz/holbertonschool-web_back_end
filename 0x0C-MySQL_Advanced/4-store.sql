-- This script creates a MySQL trigger
-- The trigger decreases the quantity of an item after adding a new order
CREATE TRIGGER after_new_order
AFTER
INSERT ON orders FOR EACH ROW
UPDATE items
SET quantity = quantity - new.number
where items.name = new.item_name;
