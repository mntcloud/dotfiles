
# A small function for testing purposes
function run
    if test $DEBUG != "True"
        set_color brblack
        echo "Running: $argv"
        set_color normal
        $argv
        and return
    end
    sleep 1
end