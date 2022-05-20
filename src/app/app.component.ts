import { Component, OnInit } from '@angular/core';
//import { PersonaService } from 'services/persona.service';

@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
})
export class AppComponent{

  public persona: Array<any> = []

  constructor(
    //private personaService:PersonaService
  ) {

    //this.personaService.getPersonas().subscribe((resp: any)=> {
      //this.personas = resp
    }//)

  }
//}



