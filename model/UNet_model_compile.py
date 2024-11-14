model.compile(optimizer = optimized, loss=total_loss, metrics=metrics)
print(model.summary())



history=model.fit(Train_dgen,
          steps_per_epoch=step_per_epoch,
          epochs=100,
          verbose=1,
          validation_data=Val_dgen,
          validation_steps=val_steps_per_epoch,
          )
