import { Component, OnInit } from '@angular/core';
declare var mapboxgl:any;
@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.page.html',
  styleUrls: ['./inicio.page.scss'],
})
export class InicioPage implements OnInit {

  constructor() { }

  ngOnInit() {
  }

  mapa2d(){
    mapboxgl.accessToken = 'pk.eyJ1Ijoia3J5ejg1MzEiLCJhIjoiY2wwemoxNG9pMDFwZDNkdzFkanAzODB1bSJ9.aNwPhHON86UUwNZrfWuWWg';
    var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11'
    });
  }
}
