import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AssignTeacherComponent } from './assign-teacher.component';

describe('AssignTeacherComponent', () => {
  let component: AssignTeacherComponent;
  let fixture: ComponentFixture<AssignTeacherComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AssignTeacherComponent]
    });
    fixture = TestBed.createComponent(AssignTeacherComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
