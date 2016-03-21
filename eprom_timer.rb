# A sort script to control my EPROM eraser (or anything esle) through the serial
# port handshake lines. Runs the eraser for 20 minutes, which is sufficient for
# most types of EPROM. Catch SIGINT and SIGTERM to make sure we don't leave the
# eraser on after a CTRL + C or `kill`.

# Wire optocoupler controlled relay board to pins 4 and 7 (RTS and GND) on a
# DB-25, or 7 and 5 on a DB-9.

# Requires `serialport` and `ruby-progressbar` gems.

# Copyright (c) 2016-03-21 The Glitch Works
# http://www.glitchwrks.com/

require 'serialport'
require 'ruby-progressbar'

SECONDS_TO_RUN = 20 * 60

port = SerialPort.new('/dev/ttyUSB0')
progress = ProgressBar.create(:title => 'EPROM Erase', :total => SECONDS_TO_RUN)
puts "Erasing for #{SECONDS_TO_RUN} seconds (#{SECONDS_TO_RUN / 60.0} minutes)..."

# Wired my cable for RTS == 0 == relay on
port.rts = 0

begin
  for seconds in 1..SECONDS_TO_RUN
    progress.increment
    sleep 1
  end
rescue SystemExit, Interrupt
  puts ' Caught interrupt, exiting...'
ensure
  port.rts = 1
  puts '...done!'
  exit
end
