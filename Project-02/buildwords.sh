#!/bin/bash
grep -E '<tr>|<td' | 
ed '/<tr>/,/<\/td>/d' |
sed -e 's@<u>@@g' -e 's@</u>@@g' |
sed -e "s@\`@\'@g" |
sed -e 's/,//g' |
tr '[:upper:]' '[:lower:]' |
sed -e 's@<td>@@g' -e 's@</td>@@g' |
tr -d '[:blank:]' |
sed '/[^pk1mnwlhaeiou]/d' |
sort -u	
