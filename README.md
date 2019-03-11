# X-Serv-18.1-Practica1
Práctica 1 (Ejercicio 18.1): Web acortadora de URLs

El funcionamiento de la aplicacion sera el siguiente:

Recurso “/”, invocado mediante GET. Devolvera una pagina HTML con un formulario.  En  ese  formulario  se  podra  escribir  una url,  que  se  enviara  alservidor mediante POST. Ademas, esa misma pagina incluira un listado detodas las URLs reales y acortadas que maneja la aplicacion en este momento.

Recurso “/”, invocado mediante POST. Si el comando POST incluye una qs(query string) que corresponda con una url enviada desde el formulario, se devolvera una pagina HTML con la URL original y la URL acortada (ambas como enlaces pinchables), y se apuntara la correspondencia (ver m ́as abajo).Si  el  POST  no  trae  una qs que se  haya  podido  generar  en  el  formulario,devolvera una p ́agina HTML con un mensaje de error.Si la URL especificada en el formulario comienza por “http://” o “https://”, se  considerara  que esa  es  la  URL  a  acortar.  Si  no  es  asi,  se  le  anadira “http://”  por  delante,  y  se  considerara  que  esa  es  la  url  a  acortar.  Por ejemplo, si  en  el  formulario  se  escribe  “http://gsyc.es”,  la  URL  a  acortar  sera “http://gsyc.es”.  Si  se  escribe  “gsyc.es”,  la  URL  a  acortar  ser ́a“http://gsyc.es”. Para determinar la URL acortada, utilizar ́a un n ́umero entero secuencial, comenzando por 0, para cada nueva peticion de acortamiento de una URL quese reciba. Si se recibe una peticion para una URL ya acortada, se devolver ́ala URL acortada que se devolvio en su momento.Ası, por ejemplo, si se quiere acortar http://gsyc.urjc.es y la aplicacion esta en el puerto 1234 de la maquina “localhost”, se invocara (mediante POST) la URL http://localhost:1234/ y en el cuerpo de esa peticion HTTP ira la qs url=http://gsyc.urjc.es si el campo donde el usuario puede escribir en el formulario tiene el nombre “URL”. Normalmente, esta invocacion POST se realizara rellenando el formulario que ofrece la aplicacion.Como respuesta, la aplicacion devolvera (en el cuerpo de la respuesta HTTP) la URL acortada, por ejemplo http://localhost:1234/3 Si a continuacion se trata de acortar la URL http://www.urjc.es mediante un procedimiento similar, se recibira como respuesta la URL acortada http://localhost:1234/4 Si se vuelve a intentar acortar la URLhttp://gsyc.urjc.escomo ya ha sido acortada previamente, se devolver ́a la misma URL corta:http://localhost:1234/3

Recursos  correspondientes  a  URLs  acortadas.  Estos  seran  numeros  con  el prefijo “/”. Cuando la aplicacion reciba un GET sobre uno de estos recursos, si el numero corresponde a una URL acortada, devolver ́a un HTTP REDIRECT a la URL real. Si no la tiene, devolver ́a HTTP ERROR “Recurso no disponible”.Por ejemplo, si se recibe http://localhost:1234/3 la aplicacion devolvera un HTTP REDIRECT a la URL http://gsyc.urjc.es

Comentario

Se recomienda utilizar dos diccionarios para almacenar las URLs reales y los numeros de las URLs acortadas. En uno de ellos, la clave de busqueda sera la URL real, y se utilizara para saber si una URL real ya est ́a acortada, y en su caso saber cual es el numero de la URL corta correspondiente. En el otro diccionario la clave de busqueda sera el numero de la URL acortada,y se utilizara para localizar las URLs reales dadas las cortas. De todas formas, son posibles (e incluso mas eficientes) otras estructuras de datos.Se recomienda realizar la aplicacion en varios pasos:

Comenzar por reconocer “GET /”, y devolver el formulario correspondiente.

Reconocer “POST /”, y devolver la pagina HTML correspondiente (con la URL real y la acortada).

Reconocer “GET /num” (para cualquier numero num), y realizar la redireccion correspondiente.

Manejar las condiciones de error y realizar el resto de la funcionalidad.
