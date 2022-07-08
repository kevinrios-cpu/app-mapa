import { Component, OnInit } from '@angular/core';
import * as mapboxgl from 'mapbox-gl';
import { environment } from 'environments/environment';
import { RestService } from '@data/services/rest.service';


@Component({
  selector: 'app-card-user',
  templateUrl: './card-user.component.html',
  styleUrls: ['./card-user.component.scss']
})
export class CardUserComponent implements OnInit {

  public datosDirecciones: Object
  marker: any;

  constructor(private RestService:RestService
  ) {
    /*this.userService.get('/direccion').subscribe (f => {
      if (!f.error) {
        this.currentUser = f.data;
      }
    })*/
   }
   
  mapa: mapboxgl.map;
  ngOnInit(
    
  ) {
    this.cargarDirecciones();
    mapboxgl.accessToken = environment.mapboxKey
     this.mapa = new mapboxgl.Map({
    container: 'mapa-mapbox', // container ID
    style: 'mapbox://styles/mapbox/streets-v11', // style URL
    center: [-70.7546298, -33.5114161], // starting position [lng, lat]
    zoom: 16, //starting zoom
});

this.marker = new mapboxgl.Marker({
})
.setLngLat([-70.7546298, -33.5114161])
.addTo( this.mapa );
}

public cargarDirecciones(){
  this.RestService.get('http://localhost:3100/direcciones').subscribe(respuesta => {
  if (respuesta = respuesta) {
    this.datosDirecciones = respuesta
  }  
  console.log(respuesta);
  })
}



    
  }

  







