CREATE TABLE sales.receipt
(
  "ID" text NOT NULL, -- Reference transactions
  "DATE" date, -- Date Transactions
  "LATTE" integer, -- Latte Drinks Qty
  "ESPRESSO" integer, -- Espresso Drinks Qty
  "ICED_LATTE" integer, -- Iced Latte Drinks Qty
  "VALE_COFFEE" integer, -- Vale Coffee Drinks Qty
  "CAPPUCCINO" integer, -- Cappuccino Drinks Qty
  "AFRICAN_COFFEE" integer, -- African Coffee Drinks Qty
  "AMERICAN_COFFEE" integer, -- American Coffee Drinks Qty
  "ICED_CAPPUCCINO" integer, -- Iced Cappuccino Drinks Qty
  "COFFEE" integer, -- Coffee Cake Qty
  "RED_VELVET" integer, -- Red Velvet Cake Qty
  "BLACK_FOREST" integer, -- Black Forest Cake Qty
  "BOSTON_CREAM" integer, -- Boston Cream Cake Qty
  "LAGOS_CHOCOLATE" integer, -- Lagos Chocolate Cake Qty
  "KILBURN_CHOCOLATE" integer, -- Kilburn Chocolate Cake Qty
  "CARLTON_CHOCOLATE" integer, -- Carlton Chocolate Cake Qty
  "QUEEN_PARK_CHOCOLATE" integer, -- Queen Park Chocolate Cake Qty
  "COST_DRINKS" real, -- Cost of Drinks Amount
  "COST_CAKES" real, -- Cost of Cakes Amount
  "SERVICE_CHARGE" real, -- Service Charge Amount
  "PAID_TAX" real, -- Paid Tax Amount
  "SUBTOTAL" real, -- Sub Total Amount
  "TOTAL_COST" real -- Total Cost Amount
)
WITH (
  OIDS=FALSE
);
ALTER TABLE sales.receipt
  OWNER TO admin;
COMMENT ON TABLE sales.receipt
  IS 'Table receipt for transactions';
COMMENT ON COLUMN sales.receipt."ID" IS 'Reference transactions';
COMMENT ON COLUMN sales.receipt."DATE" IS 'Date Transactions';
COMMENT ON COLUMN sales.receipt."LATTE" IS 'Latte Drinks Qty';
COMMENT ON COLUMN sales.receipt."ESPRESSO" IS 'Espresso Drinks Qty';
COMMENT ON COLUMN sales.receipt."ICED_LATTE" IS 'Iced Latte Drinks Qty';
COMMENT ON COLUMN sales.receipt."VALE_COFFEE" IS 'Vale Coffee Drinks Qty';
COMMENT ON COLUMN sales.receipt."CAPPUCCINO" IS 'Cappuccino Drinks Qty';
COMMENT ON COLUMN sales.receipt."AFRICAN_COFFEE" IS 'African Coffee Drinks Qty';
COMMENT ON COLUMN sales.receipt."AMERICAN_COFFEE" IS 'American Coffee Drinks Qty';
COMMENT ON COLUMN sales.receipt."ICED_CAPPUCCINO" IS 'Iced Cappuccino Drinks Qty';
COMMENT ON COLUMN sales.receipt."COFFEE" IS 'Coffee Cake Qty';
COMMENT ON COLUMN sales.receipt."RED_VELVET" IS 'Red Velvet Cake Qty';
COMMENT ON COLUMN sales.receipt."BLACK_FOREST" IS 'Black Forest Cake Qty';
COMMENT ON COLUMN sales.receipt."BOSTON_CREAM" IS 'Boston Cream Cake Qty';
COMMENT ON COLUMN sales.receipt."LAGOS_CHOCOLATE" IS 'Lagos Chocolate Cake Qty';
COMMENT ON COLUMN sales.receipt."KILBURN_CHOCOLATE" IS 'Kilburn Chocolate Cake Qty';
COMMENT ON COLUMN sales.receipt."CARLTON_CHOCOLATE" IS 'Carlton Chocolate Cake Qty';
COMMENT ON COLUMN sales.receipt."QUEEN_PARK_CHOCOLATE" IS 'Queen Park Chocolate Cake Qty';
COMMENT ON COLUMN sales.receipt."COST_DRINKS" IS 'Cost of Drinks Amount';
COMMENT ON COLUMN sales.receipt."COST_CAKES" IS 'Cost of Cakes Amount';
COMMENT ON COLUMN sales.receipt."SERVICE_CHARGE" IS 'Service Charge Amount';
COMMENT ON COLUMN sales.receipt."PAID_TAX" IS 'Paid Tax Amount';
COMMENT ON COLUMN sales.receipt."SUBTOTAL" IS 'Sub Total Amount';
COMMENT ON COLUMN sales.receipt."TOTAL_COST" IS 'Total Cost Amount';
