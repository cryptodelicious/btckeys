# Bitcoin Private Key Hacking
We have here various functions/scripts that will generate random bitcoin keys/addresses and check to see if any of them exist on the bitcoin blockchain or if any duplicate keys are ever generated.

Use the blockcypher library (already installed in venv) to query addresses via get_address_overview

# Dependencies
- blockcypher (this will automatically include the python bitcoin library)
- sqllite (optional)

# General Approach
- Generate X number of random addresses (10,000 or 100,000 or a million)
- Save addresses somewhere (text file or SQL lite)
- Loop through all the public addresses and see if any exist
	- check blockcypher to see if it exists (observe api limits)

# Virtual Environment
- activate the venv using source venv/bin/activate


