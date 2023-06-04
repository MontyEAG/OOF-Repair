--RETURN ORIGINAL OOF SOUND--
--Monty#3260--
--[[
 /$$      /$$                       /$$              
| $$$    /$$$                      | $$              
| $$$$  /$$$$  /$$$$$$  /$$$$$$$  /$$$$$$   /$$   /$$
| $$ $$/$$ $$ /$$__  $$| $$__  $$|_  $$_/  | $$  | $$
| $$  $$$| $$| $$  \ $$| $$  \ $$  | $$    | $$  | $$
| $$\  $ | $$| $$  | $$| $$  | $$  | $$ /$$| $$  | $$
| $$ \/  | $$|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$
|__/     |__/ \______/ |__/  |__/   \___/   \____  $$
                                            /$$  | $$
                                           |  $$$$$$/
                                            \______/ 
--]]

--EXIT FUNCTION--
function exit()
	print("Press Enter to exit...")
	while true do
		local input = io.read('*l')
		if input and input:match("^%s*$") then
			os.exit()
		end
	end
end

---MAIN--
os.execute('color 9')
print("====================")
print("==Return OOF Sound==")
print("===By: Monty#3260===")
print("====================")
print()
print("Enter your roblox directory")
directory = io.read()
directory = tostring(directory).. "\\content\\sounds\\ouch.ogg"
target = "ouch.ogg"
local data = io.open(target, "rb")
if not data then
	print("Failed to collect data from old ouch.ogg file.")
	return
	exit()
end
local dataContent = data:read("*all")
data:close()

local newSound = io.open(directory, "wb")
if not newSound then
  print("Failed to open original file.")
  return
  exit()
else
	newSound:write(dataContent)
	newSound:close()
	exit()
	print("OOF successfully restored <3")
end

