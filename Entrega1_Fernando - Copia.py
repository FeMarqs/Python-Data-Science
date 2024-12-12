{"nbformat":4,"nbformat_minor":0,"metadata":{"colab":{"provenance":[],"authorship_tag":"ABX9TyO5Sz+eXewGyiAz3rbcTFDC"},"kernelspec":{"name":"python3","display_name":"Python 3"},"language_info":{"name":"python"}},"cells":[{"cell_type":"markdown","source":["\n","\n","=-=-=-=-=- EXERCICIO 1 =-=-=-=-=-"],"metadata":{"id":"4U4xiMlD_WSD"}},{"cell_type":"code","source":["import datetime as dt\n","import statistics as st\n","\n","carro = {\n","    'Elaine': 40,\n","    'Isabella': 5,\n","}\n","carro_quantidade = [1, 2]\n","moto = {\n","    'Vinicius 1': 50,\n","}\n","\n","moto_quantidade = [1]\n","onibus = {\n","    'Barbara': 50,\n","    'Guilherme': 60,\n","    'Geovanne': 30,\n","    'Igor': 25,\n","    'Kaue': 15,\n","    'Luiz': 40\n","}\n","onibus_quantidade = [1, 1, 1, 1, 1, 1]\n","trem_metro = {\n","    'Isabella': 15,\n","    'Caue': 25,\n","    'Guilherme': 30,\n","    'Geovanne': 60,\n","    'Emerson': 50,\n","    'Gustavo': 40,\n","    'Vinicius 2': 20,\n","    'Kaue': 25,\n","    'Danilo': 60,\n","    'Bruno': 50,\n","}\n","trem_metro_quantidade = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]\n","outros = {\n","    'Denise': 7\n","}\n","outros_quantidade = [1]\n","#---------------------------------------------\n","carro = sum(carro.values())\n","print(carro)\n","moto = sum(moto.values())\n","print(moto)\n","onibus = sum(onibus.values())\n","print(onibus)\n","trem_metro = sum(trem_metro.values())\n","print(trem_metro)\n","outros = sum(outros.values())\n","print(outros)\n","correlacao_carro = st.correlation(carro, carro)"],"metadata":{"id":"4PyfV6SgLwPt","colab":{"base_uri":"https://localhost:8080/","height":384},"executionInfo":{"status":"error","timestamp":1733888585631,"user_tz":180,"elapsed":218,"user":{"displayName":"Kayque Pimentel","userId":"07575193919548709421"}},"outputId":"8333cb7d-3e0c-42d0-e2b6-a27fad779f53"},"execution_count":2,"outputs":[{"output_type":"stream","name":"stdout","text":["45\n","50\n","220\n","375\n","7\n"]},{"output_type":"error","ename":"TypeError","evalue":"object of type 'int' has no len()","traceback":["\u001b[0;31m---------------------------------------------------------------------------\u001b[0m","\u001b[0;31mTypeError\u001b[0m                                 Traceback (most recent call last)","\u001b[0;32m<ipython-input-2-021cd06279c2>\u001b[0m in \u001b[0;36m<cell line: 51>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     49\u001b[0m \u001b[0moutros\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0msum\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutros\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvalues\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     50\u001b[0m \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0moutros\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 51\u001b[0;31m \u001b[0mcorrelacao_carro\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcorrelation\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mcarro\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcarro\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m","\u001b[0;32m/usr/lib/python3.10/statistics.py\u001b[0m in \u001b[0;36mcorrelation\u001b[0;34m(x, y)\u001b[0m\n\u001b[1;32m    904\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    905\u001b[0m     \"\"\"\n\u001b[0;32m--> 906\u001b[0;31m     \u001b[0mn\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mx\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    907\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0mn\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    908\u001b[0m         \u001b[0;32mraise\u001b[0m \u001b[0mStatisticsError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'correlation requires that both inputs have same number of data points'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n","\u001b[0;31mTypeError\u001b[0m: object of type 'int' has no len()"]}]}]}