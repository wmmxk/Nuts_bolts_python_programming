"""
source: https://www.youtube.com/watch?v=Hw21qZs7xkA
"""


from selenium import webdriver
import time


def test_download():
    """
    after the username and password are entered. no need to enter again when accessing the same website

    :return:
    """

    url1 = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FNLDAS%2FNLDAS_FORA0125_H.002%2F1979%2F001%2FNLDAS_FORA0125_H.A19790101.1800.002.grb&FORMAT=bmM0Lw&BBOX=34%2C-110%2C34.5%2C-107.5&LABEL=NLDAS_FORA0125_H.A19790101.1800.002.grb.SUB.nc4&SHORTNAME=NLDAS_FORA0125_H&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=002&VARIABLES=APCP%2CDLWRF%2CDSWRF%2CPEVAP%2CSPFH%2CTMP%2CUGRD%2CVGRD"
    url2 = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FNLDAS%2FNLDAS_FORA0125_H.002%2F1979%2F001%2FNLDAS_FORA0125_H.A19790101.2300.002.grb&FORMAT=bmM0Lw&BBOX=34%2C-110%2C34.5%2C-107.5&LABEL=NLDAS_FORA0125_H.A19790101.2300.002.grb.SUB.nc4&SHORTNAME=NLDAS_FORA0125_H&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=002&VARIABLES=APCP%2CDLWRF%2CDSWRF%2CPEVAP%2CSPFH%2CTMP%2CUGRD%2CVGRD"
    url3 = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FNLDAS%2FNLDAS_FORA0125_H.002%2F1979%2F001%2FNLDAS_FORA0125_H.A19790101.2200.002.grb&FORMAT=bmM0Lw&BBOX=34%2C-110%2C34.5%2C-107.5&LABEL=NLDAS_FORA0125_H.A19790101.2200.002.grb.SUB.nc4&SHORTNAME=NLDAS_FORA0125_H&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=002&VARIABLES=APCP%2CDLWRF%2CDSWRF%2CPEVAP%2CSPFH%2CTMP%2CUGRD%2CVGRD"
    url4 = "https://hydro1.gesdisc.eosdis.nasa.gov/daac-bin/OTF/HTTP_services.cgi?FILENAME=%2Fdata%2FNLDAS%2FNLDAS_FORA0125_H.002%2F1979%2F001%2FNLDAS_FORA0125_H.A19790101.1400.002.grb&FORMAT=bmM0Lw&BBOX=34%2C-110%2C34.5%2C-107.5&LABEL=NLDAS_FORA0125_H.A19790101.1400.002.grb.SUB.nc4&SHORTNAME=NLDAS_FORA0125_H&SERVICE=L34RS_LDAS&VERSION=1.02&DATASET_VERSION=002&VARIABLES=APCP%2CDLWRF%2CDSWRF%2CPEVAP%2CSPFH%2CTMP%2CUGRD%2CVGRD"
    urls = [url1, url2, url3, url4]
    driver = webdriver.Chrome()
    # you will asked to enter username and password
    driver.get(url2)

    for i, url in enumerate(urls[1:]):
        print("downloading url%s-----"% (i+2))
        driver.get(url)
        # to avoid too many download tasks, wait 5 seconds
        # time.sleep(5)

    print("end---------")

test_download()
