#!/usr/bin/bash
DIR="$(cd "$(dirname "$0")" && pwd)"
cd $DIR || exit
cd ..

read -r -d '' expected_center_justification <<'EOF'
[1m
                                                                                
                            This is the first quote.                            
                                                                                
[0m
EOF

read -r -d '' expected_right_justification <<'EOF'
[1m
                                                                                
                                                        This is the first quote.
                                                                                
[0m
EOF

read -r -d '' expected_left_justification <<'EOF'
[1m
                                                                                
This is the first quote.                                                        
                                                                                
[0m
EOF

default_test=$(python -m dharma -f tests/book_tests/default_separator.txt -q 1)
right_test=$(python -m dharma -f tests/book_tests/default_separator.txt -q 1 -j right)
center_test=$(python -m dharma -f tests/book_tests/default_separator.txt -q 1 -j center)
left_test=$(python -m dharma -f tests/book_tests/default_separator.txt -q 1 -j left)

if [ "$default_test" = "$expected_center_justification" ]; then
  echo "Default test correct"
else
  echo "Default test failed"
  echo "$default_test"
fi

if [ "$center_test" = "$expected_center_justification" ]; then
  echo "Center test correct"
else
  echo "Center test failed"
  echo "$center_test"
fi

if [ "$right_test" = "$expected_right_justification" ]; then
  echo "right test correct"
else
  echo "right test failed"
  echo "$right_test"
fi

if [ "$left_test" = "$expected_left_justification" ]; then
  echo "left test correct"
else
  echo "left test failed"
  echo "$left_test"
fi
