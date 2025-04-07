USE [foodsignup-dev]; -- or foodsignup-qa

GO

BEGIN TRANSACTION;

-- Step 1: Add VendorId column to VendorOrder table
ALTER TABLE VendorOrder
ADD VendorId INT;

-- Step 2: Update VendorOrder with appropriate VendorId based on MenuDetailId
UPDATE vo
SET vo.VendorId = ma.VendorId
FROM VendorOrder vo
JOIN MenuAvailability ma ON vo.MenuDetailId = ma.MenuDetailId
JOIN Menu m ON ma.MenuId = m.MenuId
WHERE vo.IsCancelled = 0; -- Assuming only active orders need to be updated

-- Step 3: Add foreign key constraint
ALTER TABLE VendorOrder
ADD CONSTRAINT FK_VendorOrder_Vendors FOREIGN KEY (VendorId) 
REFERENCES Vendors(VendorId);

-- Step 4: Set VendorId to NOT NULL if this is a requirement (optional)
-- ALTER TABLE VendorOrder
-- ALTER COLUMN VendorId INT NOT NULL;

COMMIT TRANSACTION;
GO

PRINT 'VendorId column added to VendorOrder table and updated successfully.';
GO