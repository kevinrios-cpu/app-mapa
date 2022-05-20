import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'

@Injectable({
  providedIn: 'root'
})
export class PersonaService {
  //ingresar url de api rest :c
  _url =''
  constructor(
    private http: HttpClient
  ) {
    console.log('Servicio persona')
   }
   getPersonas(){
     let header= new HtppHeaders()
       .set('Type-content', 'aplication/json')
  
       return this.http.get(this._url,{
         headers: header
       })
    }
}
