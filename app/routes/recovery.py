@login_bp.route('/recover', methods=['GET', 'POST'])
def recover_password():
    form = RecoverForm()
    if form.validate_on_submit():
        input_data = form.identifier.data
        # Aqui você pode buscar tanto por e-mail quanto telefone
        user = User.query.filter((User.email == input_data) | (User.phone == input_data)).first()

        if user:
            # Aqui você pode decidir: enviar e-mail ou mensagem pelo WhatsApp
            flash('Enviamos instruções para recuperação no seu contato.', 'info')
            # Exemplo: enviar_whatsapp(user.phone, "Clique no link para redefinir...")
        else:
            flash('Usuário não encontrado.', 'warning')
    return render_template('recover_password.html', form=form)
