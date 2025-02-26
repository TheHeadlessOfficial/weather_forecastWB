import os
import requests
import time
# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wbforecast.lock"
# Check for file lock
try:
    open(lock_file, 'w').close()
    ################################ set your latitude, longitude and APPID (don't delete apostrophes)
    mylat = 
    mylon = 
    myAPPID = ''
    ################################ pattern url forecast
    url = 'https://api.weatherbit.io/v2.0/forecast/daily?lat=' + str(mylat) + '&lon=' + str(mylon) + '&key=' + myAPPID
    res = requests.get(url).json()
    data = res
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set paths
    home = '/home/'
    conky = '/.conky/'
    ptemp = conky + "weather/Weatherbit/forecast/"
    ptemp2 = conky + "weather/Weatherbit/"
    ptemp3 = " $HOME" + conky + "weather/Weatherbit/"
    ptemp4 = " $HOME" + conky + "weather/Weatherbit/forecast/"
    #                   set the paths for the ERROR
    perr = home + homename + ptemp + '-error.txt'
    #                   set the paths for the GENERAL section
    pgen = home + homename + ptemp + '-general.txt'
    #                   set the paths for the FORECAST section
    pforecast = home + homename + ptemp + "-forecastraw.txt"
    #                   set the paths for the FORECAST clean data section
    pforecastclean = home + homename + ptemp + "forecastclean.txt"
    #                   set the paths for the DEW POINT
    pdewp = home + homename + ptemp + 'forecastdewpt.txt'
    #                   set the paths for the UVI INDEX
    puvi = home + homename + ptemp + 'forecastuv.txt'
    ################################ get data for ERROR section
    responseHTTP = requests.get(url)
    # get status code
    status_code = responseHTTP.status_code
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    ################################ set variables
    vforecast = 7 # number of days
    groupd = 45 # number of rows for 1 day
    temporary = ''
    vtext = 'n/a'
    ################################ create variables for GENERAL data
    lat = 0
    lon = 0
    tz = ''
    cityname = ''
    countrycode = ''
    statecode = ''
    ################################ get data for GENERAL section
    lat = data['lat']
    lon = data['lon']
    tz = data['timezone']
    cityname = data['city_name']
    countrycode = data['country_code']
    statecode = data['state_code']
    ################################ write raw data for GENERAL section
    fo = open(pgen, 'w')
    fo.write('lat: {}\n'.format(lat))
    fo.write('lon: {}\n'.format(lon))
    fo.write('TimeZone: {}\n'.format(tz))
    fo.write('Cityname: {}\n'.format(cityname))
    fo.write('Countrycode: {}\n'.format(countrycode))
    fo.write('Statecode: {}\n'.format(statecode))
    fo.close()
    ################################ create array for FORECAST daily data
    fmoonrisets = []
    fmoonrisets2 = []
    fwindcdir = []
    frh = []
    fpres = []
    fhightemp = []
    fsunsetts = []
    fsunsetts2 = []
    fozone = []
    fmoonphase = []
    fwindgustspd = []
    fsnowdepth = []
    fclouds = []
    fts = []
    fts2 = []
    fsunrisets = []
    fsunrisets2 = []
    fappmintemp = []
    fwindspd = []
    fpop = []
    fwindcdirfull = []
    fslp = []
    fmoonlunation = []
    fvaliddate = []
    fappmaxtemp = []
    fvis = []
    fdewpt = []
    fsnow = []
    fuv = []
    fwicon = []
    fwcode = []
    fwdesc = []
    fwinddir = []
    fmaxdhi = []
    fcloudshi = []
    fprecip = []
    flowtemp = []
    fmaxtemp = []
    fmoonsetts = []
    fmoonsetts2 = []
    fdatetime = []
    ftemp = []
    fmintemp = []
    cloudsmid = []
    fcloudslow = []
    ################################ get data for FORECAST section
    for i in range(0, vforecast):
        fappmaxtemp.append(data['data'][i]['app_max_temp'])
        fappmintemp.append(data['data'][i]['app_min_temp'])
        fclouds.append(data['data'][i]['clouds'])
        fcloudshi.append(data['data'][i]['clouds_hi'])
        fcloudslow.append(data['data'][i]['clouds_low'])
        cloudsmid.append(data['data'][i]['clouds_mid'])
        fdatetime.append(data['data'][i]['datetime'])
        fdewpt.append(data['data'][i]['dewpt'])
        fhightemp.append(data['data'][i]['high_temp'])
        flowtemp.append(data['data'][i]['low_temp'])
        try:
            fmaxdhi.append(data['data'][i]['max_dhi'])
            if fmaxdhi[i] is None:
                fmaxdhi[i] = vtext
        except:
            fmaxdhi.append(vtext) 
        fmaxtemp.append(data['data'][i]['max_temp'])
        fmintemp.append(data['data'][i]['min_temp'])
        fmoonphase.append(data['data'][i]['moon_phase'])
        fmoonlunation.append(data['data'][i]['moon_phase_lunation'])
        fmoonrisets.append(data['data'][i]['moonrise_ts'])
        fmoonrisets2.append(data['data'][i]['moonrise_ts'])
        fmoonsetts.append(data['data'][i]['moonset_ts'])
        fmoonsetts2.append(data['data'][i]['moonset_ts'])
        fozone.append(data['data'][i]['ozone'])
        fpop.append(data['data'][i]['pop'])
        fprecip.append(data['data'][i]['precip'])
        fpres.append(data['data'][i]['pres'])
        frh.append(data['data'][i]['rh'])
        fslp.append(data['data'][i]['slp'])
        fsnow.append(data['data'][i]['snow'])
        fsnowdepth.append(data['data'][i]['snow_depth'])
        fsunrisets.append(data['data'][i]['sunrise_ts'])
        fsunrisets2.append(data['data'][i]['sunrise_ts'])
        fsunsetts.append(data['data'][i]['sunset_ts'])
        fsunsetts2.append(data['data'][i]['sunset_ts'])
        ftemp.append(data['data'][i]['temp'])
        fts.append(data['data'][i]['ts'])
        fts2.append(data['data'][i]['ts'])
        fuv.append(data['data'][i]['uv'])
        fvaliddate.append(data['data'][i]['valid_date'])
        fvis.append(data['data'][i]['vis'])
        fwcode.append(data['data'][i]['weather']['code'])
        fwicon.append(data['data'][i]['weather']['icon'])
        fwdesc.append(data['data'][i]['weather']['description'])
        fwindcdir.append(data['data'][i]['wind_cdir'])
        fwindcdirfull.append(data['data'][i]['wind_cdir_full'])
        fwinddir.append(data['data'][i]['wind_dir'])
        fwindgustspd.append(data['data'][i]['wind_gust_spd'])
        fwindspd.append(data['data'][i]['wind_spd'])
    ################################ write raw data for FORECAST section
    fo = open(pforecast, 'w')
    for i in range(0, vforecast):
        fo.write('moonrisetime: {}\n'.format(fmoonrisets[i]))
        fmoonrisets2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fmoonrisets2[i]))
        fo.write('moonrisetime2: {}\n'.format(fmoonrisets2[i]))
        fo.write('winddirectionabb: {}\n'.format(fwindcdir[i]))
        fo.write('humidity: {}\n'.format(frh[i]))
        fo.write('pressure: {}\n'.format(fpres[i]))
        fo.write('hightemp: {}\n'.format(fhightemp[i]))
        fo.write('sunsettime: {}\n'.format(fsunsetts[i]))
        fsunsetts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fsunsetts2[i]))
        fo.write('sunsettime2: {}\n'.format(fsunsetts2[i]))
        fo.write('ozone: {}\n'.format(fozone[i]))
        fo.write('moonphaseillumi: {}\n'.format(fmoonphase[i]))
        #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
        fwindgustspd[i] = float(round(fwindgustspd[i] * 3.6, 2))
        fo.write('windgustspd: {}\n'.format(fwindgustspd[i]))
        fo.write('snowdepth: {}\n'.format(fsnowdepth[i]))
        fo.write('clouds: {}\n'.format(fclouds[i]))
        fo.write('forecaststart: {}\n'.format(fts[i]))
        fts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fts2[i]))
        fo.write('forecaststart2: {}\n'.format(fts2[i]))
        fo.write('sunrisetime: {}\n'.format(fsunrisets[i]))
        fsunrisets2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fsunrisets2[i]))
        fo.write('sunrisetime2: {}\n'.format(fsunrisets2[i]))
        fo.write('tempfeelsmin: {}\n'.format(fappmintemp[i]))
        #                   transform in Km/h (if you want m/s put a # at the beginning of the next row)
        fwindspd[i] = float(round(fwindspd[i] * 3.6, 2))
        fo.write('windspd: {}\n'.format(fwindspd[i]))
        fo.write('pop: {}\n'.format(fpop[i]))
        fo.write('winddirectionalfull: {}\n'.format(fwindcdirfull[i]))
        fo.write('sealevelpressure: {}\n'.format(fslp[i]))
        fo.write('moonlunation: {}\n'.format(fmoonlunation[i]))
        fo.write('forecastvalidity: {}\n'.format(fvaliddate[i]))
        fo.write('tempfeelsmax: {}\n'.format(fappmaxtemp[i]))
        fo.write('visibility: {}\n'.format(fvis[i]))
        fo.write('dewpoint: {}\n'.format(fdewpt[i]))
        fo.write('snow: {}\n'.format(fsnow[i]))
        fo.write('uvindex: {}\n'.format(fuv[i]))
        fo.write('weathericon: {}\n'.format(fwicon[i]))
        fo.write('weathercode: {}\n'.format(fwcode[i]))
        fo.write('weatherdesc: {}\n'.format(fwdesc[i]))
        fo.write('windirection: {}\n'.format(fwinddir[i]))
        fo.write('maxDHI: {}\n'.format(fmaxdhi[i]))
        fo.write('cloudshigh: {}\n'.format(fcloudshi[i]))
        # round the decimal for precipitation
        fprecip[i] = str(round(fprecip[i], 2))
        fo.write('precipitation: {}\n'.format(fprecip[i]))
        fo.write('lowtemp: {}\n'.format(flowtemp[i]))
        fo.write('tempmax: {}\n'.format(fmaxtemp[i]))
        fo.write('moonsettime: {}\n'.format(fmoonsetts[i]))
        fmoonsetts2[i]  = time.strftime("%d-%B-%Y %H:%M:%S", time.localtime(fmoonsetts2[i]))
        fo.write('moonsettime2: {}\n'.format(fmoonsetts2[i]))
        fo.write('forecastvaliddate: {}\n'.format(fdatetime[i]))
        fo.write('temp: {}\n'.format(ftemp[i]))
        fo.write('tempmin: {}\n'.format(fmintemp[i]))
        fo.write('cloudsmid: {}\n'.format(cloudsmid[i]))
        fo.write('cloudslow: {}\n'.format(fcloudslow[i]))
    fo.close()
    ################################ write clean data for FORECAST section
    fo = open(pforecastclean, 'w')
    for i in range(0, vforecast):
        fo.write('{}\n'.format(fmoonrisets[i]))
        fo.write('{}\n'.format(fmoonrisets2[i]))
        fo.write('{}\n'.format(fwindcdir[i]))
        fo.write('{}\n'.format(frh[i]))
        fo.write('{}\n'.format(fpres[i]))
        fo.write('{}\n'.format(fhightemp[i]))
        fo.write('{}\n'.format(fsunsetts[i]))
        fo.write('{}\n'.format(fsunsetts2[i]))
        fo.write('{}\n'.format(fozone[i]))
        fo.write('{}\n'.format(fmoonphase[i]))
        fo.write('{}\n'.format(fwindgustspd[i]))
        fo.write('{}\n'.format(fsnowdepth[i]))
        fo.write('{}\n'.format(fclouds[i]))
        fo.write('{}\n'.format(fts[i]))
        fo.write('{}\n'.format(fts2[i]))
        fo.write('{}\n'.format(fsunrisets[i]))
        fo.write('{}\n'.format(fsunrisets2[i]))
        fo.write('{}\n'.format(fappmintemp[i]))
        fo.write('{}\n'.format(fwindspd[i]))
        fo.write('{}\n'.format(fpop[i]))
        fo.write('{}\n'.format(fwindcdirfull[i]))
        fo.write('{}\n'.format(fslp[i]))
        fo.write('{}\n'.format(fmoonlunation[i]))
        fo.write('{}\n'.format(fvaliddate[i]))
        fo.write('{}\n'.format(fappmaxtemp[i]))
        fo.write('{}\n'.format(fvis[i]))
        fo.write('{}\n'.format(fdewpt[i]))
        fo.write('{}\n'.format(fsnow[i]))
        fo.write('{}\n'.format(fuv[i]))
        fo.write('{}\n'.format(fwicon[i]))
        fo.write('{}\n'.format(fwcode[i]))
        fo.write('{}\n'.format(fwdesc[i]))
        fo.write('{}\n'.format(fwinddir[i]))
        fo.write('{}\n'.format(fmaxdhi[i]))
        fo.write('{}\n'.format(fcloudshi[i]))
        fo.write('{}\n'.format(fprecip[i]))
        fo.write('{}\n'.format(flowtemp[i]))
        fo.write('{}\n'.format(fmaxtemp[i]))
        fo.write('{}\n'.format(fmoonsetts[i]))
        fo.write('{}\n'.format(fmoonsetts2[i]))
        fo.write('{}\n'.format(fdatetime[i]))
        fo.write('{}\n'.format(ftemp[i]))
        fo.write('{}\n'.format(fmintemp[i]))
        fo.write('{}\n'.format(cloudsmid[i]))
        fo.write('{}\n'.format(fcloudslow[i]))
    fo.close()
    ################################ calculate FORECAST dew point color and write it
    color = 'white'
    #      calculate the DEW POINT color font based on index
    fo = open(pdewp, 'w')
    for i in range(0, vforecast):
        value = fdewpt[i]
        if (value < 19):
            color = 6
        elif (value >=19 and value < 22):
            color = 9
        elif (value >=22):
            color = 4
        else:
            color = 'white'
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
    ################################ calculate FORECAST UV index color and write it
    fo = open(puvi, 'w')
    for i in range(0, vforecast):
        value = fuv[i]
        if (value >=0 and value < 3):
            color = 6
        elif (value >=3 and value < 6):
            color = 9
        elif (value >=6 and value < 8):
            color = 3
        elif (value >=8 and value < 11):
            color = 4
        elif (value >= 11):
            color = 0
        else:
            color = 2
        fo.write('{}\n'.format(value))
        fo.write('{}\n'.format(color))
    fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed