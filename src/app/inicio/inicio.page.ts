import { Component, OnInit } from '@angular/core';
declare var mapboxgl:any;
import { MenuController } from '@ionic/angular';


@Component({
  selector: 'app-inicio',
  templateUrl: './inicio.page.html',
  styleUrls: ['./inicio.page.scss'],
})
export class InicioPage implements OnInit {

  constructor(private menu: MenuController) { }

  openFirst() {
    this.menu.enable(true, 'first');
    this.menu.open('first');
  }

  openEnd() {
    this.menu.open('end');
  }

  openCustom() {
    this.menu.enable(true, 'custom');
    this.menu.open('custom');
  }

  ngOnInit() {
    mapboxgl.accessToken = 'pk.eyJ1Ijoia3J5ejg1MzEiLCJhIjoiY2wwemoxNG9pMDFwZDNkdzFkanAzODB1bSJ9.aNwPhHON86UUwNZrfWuWWg';
    var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11'
    });
  }

}
