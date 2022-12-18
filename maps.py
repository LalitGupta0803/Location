import streamlit as st
from streamlit.components.v1 import html
from bokeh.models.widgets import Button
from bokeh.models import CustomJS
from streamlit_bokeh_events import streamlit_bokeh_events

# def getCurrentLocation():
#     loc_button = Button(label="Share Location")
#     loc_button.js_on_event("button_click", CustomJS(code="""
#         navigator.geolocation.getCurrentPosition(
#             (loc) => {
#                 document.dispatchEvent(new CustomEvent("GET_LOCATION", {detail: {lat: loc.coords.latitude, lon: loc.coords.longitude}}))
#             }
#         )
#         """))
#     result = streamlit_bokeh_events(
#         loc_button,
#         events="GET_LOCATION",
#         key="get_location",
#         refresh_on_update=False,
#         override_height=75,
#         debounce_time=0)
#     if result and result !=None:
#         return str(result["GET_LOCATION"]["lat"])+","+str(result["GET_LOCATION"]["lon"])
# data = getCurrentLocation()
# if data != None:
#     inital = data
def drawMap(initial,final):
    pureHTML="""
        <style>#googleMap{{
                width: 100%;
                height: 1000px;
            }} 
        </style>
        <div id="googleMap">
        </div>
        <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAPHaR6gpYen-f7Qc97kIyMNnSliQZjuxI&libraries=places"></script>
        <script>
            var mylatlng = {{lat:28.6785357
                            ,lng:77.5106955}};
    var mapOptions = {{
        center : mylatlng,
        zoom:18,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }}
    var map = new google.maps.Map(document.getElementById("googleMap"), mapOptions);
    var directionsService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer();
    directionsDisplay.setMap(map);
    function calcRoute(){{
        var request = {{
            origin:"{}",
            destination:"{}",
            travelMode : google.maps.TravelMode.DRIVING,
            unitSystem : google.maps.UnitSystem.IMPERIAL
        }}
        directionsService.route(request,(result,status)=>{{
            if (status == google.maps.DirectionsStatus.OK){{
                directionsDisplay.setDirections(result);

            }}else{{
                directionsDisplay.setDirections({{routes:[]}})
                map.setCenter(mylatlng);
            }}
        }});
    }}
    calcRoute();
        </script>
    """.format(initial,final)
    html(pureHTML,height=500)


inital = st.text_input("Enter Inital Point")
final = st.text_input("Enter Destination")
data = st.button("Submit")
if data:
    drawMap(inital,final)

