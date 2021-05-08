#!/bin/bash
curl -X GET "https://api.openweathermap.org/data/2.5/weather?lat=35&lon=139&appid=bb229e96a48520d679f8a40d072143eb" >>$HOME/weather.json
