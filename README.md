rain-forecast
=============

Gives a simple rain forecast based on data by forecast.io and using the
[Python wrapper by Ze'ev Gilovitz and Tim Heckman](https://github.com/ZeevG/python-forcast.io).

 * The bars are the probability of there being precipitation at the given time.
 * The description on the right is the strength of the precipitation if there is any.

1. Create your API key at http://developer.forecast.io
2. Enter the API key in weather.py
3. Replace the latitude/longitude values with where you want the rain forecast for.
4. Run weather.py

Requires Python 2.7 or higher

Example output:

    13 ███████                                            moderate
    14 ██████                                             moderate
    15 ██████                                             moderate
    16 ███████                                            moderate
    17 █████████                                          moderate
    18 ██████████                                         moderate
    19 ███████████                                        moderate
    20 ███████████                                        moderate
    21 ██████████                                         moderate
    22 █████████                                          light
    23 ██████                                             light
    00 ████                                               light
    01                                                    
    02                                                    
    03                                                    
    04                                                    
    05                                                    
    06                                                    
    07                                                    
    08                                                    
    09                                                    
    10                                                    
    
     0.0  0.1  0.2  0.3  0.4  0.5  0.6  0.7  0.8  0.9  1.0
     
## License for weather.py

Do whatever you want as long as you don't hold me liable for anything.

## License for Python wrapper (forecastio.py)

### License (BSD 2-clause)

Copyright (c) 2013, Ze'ev Gilovitz, Tim Heckman
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.


THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.