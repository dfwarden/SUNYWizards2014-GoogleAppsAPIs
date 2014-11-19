<?php

$log_file = 'path-to-output-log-file';

$headers = apache_request_headers();
$body = file_get_contents('php://input');
$payload = json_decode($body, $assoc=true);
if (json_last_error() != JSON_ERROR_NONE)
	exit;

# Headers and payload have been successfully loaded in associative arrays.
# Merge, append newline and append to log file.
if (is_array($payload))
    $event = array_merge($headers, $payload);
else
    $event = $headers;
$event_string = json_encode($event) . "\n";
file_put_contents($log_file, $event_string, FILE_APPEND);

?>
