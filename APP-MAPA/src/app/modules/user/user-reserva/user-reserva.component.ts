import { Component, OnInit } from '@angular/core';
import { FormGroup } from '@angular/forms';
import { RestService } from '@data/services/rest.service';

@Component({
  selector: 'app-user-reserva',
  templateUrl: './user-reserva.component.html',
  styleUrls: ['./user-reserva.component.scss']
})
export class UserReservaComponent implements OnInit {
  public form: FormGroup;

  constructor(private RestService:RestService) { }

  ngOnInit() {
    this.cargarData();
  }
  public cargarData(){
    this.RestService.get('http://localhost:3100/reserva')
    .subscribe(respuesta => {
      console.log(respuesta);
    })
  }
  public enviarData(){
    this.RestService.post('http://localhost:3100/reserva',
    this.form.value
    )
    .subscribe(respuesta => {
      console.log('Solicitud de reserva enviada!!!');
    })
  }

}
