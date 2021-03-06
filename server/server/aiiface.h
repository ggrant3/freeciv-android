/***********************************************************************
 Freeciv - Copyright (C) 1996 - A Kjeldberg, L Gregersen, P Unold
   This program is free software; you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation; either version 2, or (at your option)
   any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
***********************************************************************/
#ifndef FC__AIIFACE_H
#define FC__AIIFACE_H

#include "ai.h" /* incident_type */

/* Not part of ai.h as this must be server only */
#define FC_AI_DEFAULT_NAME "default"

void ai_init(void);

void call_incident(enum incident_type type, struct player *violator,
                   struct player *victim);

#endif /* FC__AIIFACE_H */
