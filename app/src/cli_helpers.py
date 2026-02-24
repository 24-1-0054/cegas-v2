from logger import logger
import traceback, re

def attr_input(attr, attr_owner, datatype=str, prompt=None, nullable=False, 
               nullable_prompt:str="(leave blank if none): ", fk_ref=None, 
               max=128):
    """Definition: Prompts attributes for user entries.\n
    Written to handle SQL constraints easily.\n
    Note: `fk_ref` is required for FKs. It takes\n
    a list of tuples to check if an FK is there.\n
    Note: `attr` and `attr_owner` are ignored if `prompt` is set"""
    if not prompt:
        # Roundabout way to add formattable default params
        prompt = f"What is the {attr} of the {attr_owner}? " 

    if nullable:
        prompt += nullable_prompt

    output = input(prompt).strip()

    if not output and not nullable:
        raise ValueError("Input of attribute set to NOT NULL is NULL.")

    # Prevent conversion errors on null non-strings.
    if not output and nullable and datatype != str: 
        return ""
    if fk_ref and datatype(output) not in [row[0] for row in fk_ref]:
        logger.tee(datatype(output), [row[0] for row in fk_ref])
        raise ValueError("Foreign key not found.")
    return datatype(output)

def input_err(error: Exception, msg=None):
    """A convenient function for a repetitive error message."""
    logger.tee("ValueError: ", error)
    logger.log(traceback.format_exc())
    print(msg or "Your invalid input was not submitted to the database.")

def is_email_format(email: str):
    """A function that uses regex to check if a string is formatted like an
    email."""

    # see full regex explanation at: https://regex101.com/
    # 
    # ^ asserts position at start of a line
    # \S matches any non-whitespace character (equivalent to [^\r\n\t\f\v ])
    # + matches the previous token between one and unlimited times
    # @ matches the character @ literally
    # \. matches the character .
    # $ asserts position at the end of a line

    if re.match(r"^\S+@\S+\.\S+$", email):
        if email.count('@') < 2: # email addresses can only have one '@'
            return True
    return False

