-- TABLE
CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100),
    phone_number VARCHAR(20)
);

-- 1. SEARCH FUNCTION
CREATE OR REPLACE FUNCTION search_contacts(p text)
RETURNS TABLE(username VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT username, phone_number
    FROM contacts
    WHERE username ILIKE '%' || p || '%'
       OR phone_number ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;

-- 2. PAGINATION FUNCTION
CREATE OR REPLACE FUNCTION get_contacts_paginated(limit_val INT, offset_val INT)
RETURNS TABLE(username VARCHAR, phone_number VARCHAR) AS $$
BEGIN
    RETURN QUERY
    SELECT username, phone_number
    FROM contacts
    LIMIT limit_val OFFSET offset_val;
END;
$$ LANGUAGE plpgsql;

-- 3. UPSERT PROCEDURE
CREATE OR REPLACE PROCEDURE upsert_contact(p_name VARCHAR, p_phone VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM contacts WHERE username = p_name) THEN
        UPDATE contacts SET phone_number = p_phone WHERE username = p_name;
    ELSE
        INSERT INTO contacts(username, phone_number) VALUES(p_name, p_phone);
    END IF;
END;
$$;

-- 4. BULK INSERT PROCEDURE
CREATE OR REPLACE PROCEDURE insert_bulk_contacts(p_names VARCHAR[], p_phones VARCHAR[])
LANGUAGE plpgsql AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(p_names, 1) != array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have same length';
    END IF;

    FOR i IN 1..array_length(p_names, 1) LOOP
        IF p_phones[i] ~ '^[0-9]+$' THEN
            CALL upsert_contact(p_names[i], p_phones[i]);
        ELSE
            RAISE NOTICE 'Invalid phone: %', p_phones[i];
        END IF;
    END LOOP;
END;
$$;

-- 5. DELETE PROCEDURE
CREATE OR REPLACE PROCEDURE delete_contact_proc(p_value VARCHAR)
LANGUAGE plpgsql AS $$
BEGIN
    DELETE FROM contacts
    WHERE username = p_value OR phone_number = p_value;
END;
$$;